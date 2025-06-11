
---

## 📁 2. `scripts/database/README.md`

Create:

```markdown
# 🗂️ scripts/database

This folder contains all files related to database storage using Oracle:

## Files

- `create_tables_oracle.sql`  
  SQL schema for `banks` and `reviews` tables.

- `upload_to_oracle.py`  
  Python script that connects to Oracle DB using `oracledb`, inserts >1000 reviews with foreign key mapping.

- `dump_bank_reviews.sql`  
  Placeholder or exported SQL dump from Oracle.

## Dependencies

```bash
pip install oracledb pandas
