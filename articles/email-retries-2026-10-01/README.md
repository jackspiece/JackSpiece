# A timeout is not a failed send

A practical test of email retries and idempotency

AI-written technical demonstration prepared for jackspiece. The experiment below is synthetic, runs locally and sends no email.

A receipt request times out. The obvious recovery is to send it again. That is also how you can end up with two receipts: the provider may have accepted the first request before its response disappeared. The client knows that it did not receive an answer. It does not yet know what the provider did.

I built a small Python experiment to make that gap visible. It has no network tricks and no email account. A SQLite table represents messages accepted by an imaginary provider. The provider commits its record, then deliberately raises TimeoutError instead of returning the result. Retrying without a stable request key creates two records. Retrying with the original key leaves one.

This is the failure I would test before adding a retry decorator. A decorator can repeat an operation very reliably while the operation itself is unsafe to repeat.

## Break the reply after the commit

The timing of the injected fault matters. A test that raises before storing anything only proves that a later attempt can succeed. It never exercises the uncomfortable case where the side effect happened but the acknowledgement did not arrive.

The demo has two tables: accepted stores the payload and its generated ID; requests binds an idempotency key to that payload and ID. In the keyed path, both records commit in one transaction. The lost-reply exception is raised afterward. A second request can therefore recover the original ID even though the first caller saw an exception.

Here is the essential test. The fixture creates a fresh temporary database for each test; provider is an instance of the local simulator, and payload contains an invented recipient and subject.

```python
with self.assertRaises(TimeoutError):
    provider.accept(payload, key="receipt/42",
                    lose_reply=True)
original_id = provider.accept(payload, key="receipt/42")
assert provider.accept(payload, key="receipt/42") == original_id
assert provider.count() == 1
```

## Same intention means the same key

Generating a new UUID inside the retry loop defeats this design. Each attempt arrives with a different identity, so the provider has no reason to connect it to the previous attempt. That variant in the test suite records two acceptances despite using a key on every call.

A useful key names the business action: receipt/42, for example, means the receipt for order 42. Persist that identifier before attempting the send, alongside the immutable payload. A crashed worker should resume the same action, not invent another identity when it restarts.

Do not use the recipient address alone. The same person may legitimately need two different messages. And do not silently treat a changed payload as a retry. In the demo, reusing receipt/42 with a different subject raises KeyConflict. Otherwise a caller could believe it sent the revised message while receiving the ID of the old one.

The fixture compares sorted JSON with compact separators. That makes dictionary insertion order irrelevant for these simple string fields. It is not a universal canonicalization scheme for arbitrary objects, numbers or application-specific equivalence. A production API needs to define that contract explicitly.

## The race has to happen inside the test

A check-then-insert sequence is still vulnerable if two workers can both observe an absent key. The demo starts a write transaction with BEGIN IMMEDIATE before checking it. SQLite permits one writer at a time; a competing writer may wait or encounter SQLITE_BUSY. The test uses a ten-second connection timeout, not unlimited retries. [1]

Twelve threads are released together with a barrier. They call the same provider with the same key through separate database connections. The assertions require one accepted row and one shared response ID. All twelve calls passed those assertions in the recorded run.

This deliberately modest setup tests the implementation actually included here. It does not establish behavior across regions, prove a latency bound or predict how a distributed production database will handle the same race.

## The provider boundary still matters

The most dangerous adaptation would be to put a real SMTP send between BEGIN and COMMIT and declare the problem solved. SQLite cannot roll back an email that another service has already accepted. Our transaction only owns the local acceptance ledger.

At an external boundary, use the provider’s documented idempotency facility where available and retain the same logical request identity across retries. Resend, for example, documents idempotency keys for its email and batch endpoints, with a 24-hour retention window. That window is part of the guarantee: a delayed retry beyond it needs reconciliation rather than an assumption that the provider still remembers the key. [2]

A durable outbox can preserve your intention to send across a process crash. It does not, by itself, eliminate the gap between external acceptance and your worker recording success. If the provider cannot deduplicate or let you reconcile an uncertain result, you need an explicit policy for that uncertainty. A receipt that might be duplicated and a notification that must never be duplicated may warrant different choices.

HTTP does not supply a blanket permission to retry every POST. RFC 9110 ties automatic retry of non-idempotent requests to knowing the request is safe to repeat or knowing the original was never applied. That distinction belongs in the client’s recovery logic, not just its exception handler. [3]

## What the tests actually established

All nine tests passed. They cover a lost reply after commit, a naive duplicate, a new-key duplicate, changed-payload rejection, rollback before commit, persistence after reopening the database, twelve concurrent callers, distinct business actions and JSON key-order independence.

The command is python -m unittest -v in the accompanying code directory. It uses only Python’s standard library. No external email service was tested, and there is no claim about inbox delivery.

The practical rule is small: preserve the identity of the action, and make an unknown outcome a state your system can represent. Before you retry a send, you should be able to explain why this next attempt will recover the old result rather than create a new one.

## Sources

[1] SQLite transaction documentation, sections 2.1 and 2.2. https://www.sqlite.org/lang_transaction.html

[2] Resend idempotency key documentation. https://resend.com/docs/dashboard/emails/idempotency-keys

[3] RFC 9110 section 9.2.2, Idempotent Methods. https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2

Documentation checked October 1, 2026. Test evidence: test-results.txt; implementation: retry_demo.py; cases: test_retry_demo.py.

## Run the experiment

Download [retry_demo.py](retry_demo.py) and [test_retry_demo.py](test_retry_demo.py) into the same directory, then run `python -m unittest -v`. The [recorded test output](test-results.txt) is included. Python 3.10 or newer is recommended. No third-party packages or credentials are needed.
