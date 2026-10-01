"""Synthetic email-provider acceptance ledger. No network or real email sending."""
import json
import sqlite3
from pathlib import Path

class KeyConflict(ValueError):
    pass

class Provider:
    def __init__(self, path):
        self.path = str(path)
        with sqlite3.connect(self.path) as db:
            db.execute('CREATE TABLE IF NOT EXISTS accepted (id INTEGER PRIMARY KEY, payload TEXT NOT NULL)')
            db.execute('CREATE TABLE IF NOT EXISTS requests (key TEXT PRIMARY KEY, payload TEXT NOT NULL, response_id INTEGER NOT NULL)')

    def accept(self, payload, key=None, lose_reply=False, fail_before_commit=False):
        """Atomically record provider acceptance and a key, then optionally lose its reply."""
        encoded = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
        db = sqlite3.connect(self.path, timeout=10)
        try:
            db.execute('BEGIN IMMEDIATE')
            previous = db.execute('SELECT payload,response_id FROM requests WHERE key=?',(key,)).fetchone() if key is not None else None
            if previous:
                if previous[0] != encoded:
                    raise KeyConflict('Key already identifies a different payload')
                response_id = previous[1]
            else:
                response_id = db.execute('INSERT INTO accepted(payload) VALUES (?)',(encoded,)).lastrowid
                if key is not None:
                    db.execute('INSERT INTO requests VALUES (?,?,?)',(key,encoded,response_id))
            if fail_before_commit:
                raise RuntimeError('Simulated crash before transaction commit')
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
        if lose_reply:
            raise TimeoutError('Simulated response lost AFTER commit')
        return response_id

    def count(self):
        with sqlite3.connect(self.path) as db:
            return db.execute('SELECT COUNT(*) FROM accepted').fetchone()[0]
