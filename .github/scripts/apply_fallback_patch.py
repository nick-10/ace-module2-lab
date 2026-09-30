#!/usr/bin/env python3
import sys

def main():
    scan_path = sys.argv[1] if len(sys.argv) > 1 else "routes"
    file_path = f"{scan_path}/search.ts"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        target = "models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)"
        replacement = "models.sequelize.query('SELECT * FROM Products WHERE ((name LIKE :criteria OR description LIKE :criteria) AND deletedAt IS NULL) ORDER BY name', { replacements: { criteria: `%${criteria}%` } })"
        if target in content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content.replace(target, replacement))
            print(f"Successfully applied fallback security patch to {file_path}")
        else:
            print(f"Target pattern not found in {file_path} or already patched.")
    except Exception as e:
        print(f"Error applying fallback patch: {e}")

if __name__ == "__main__":
    main()
