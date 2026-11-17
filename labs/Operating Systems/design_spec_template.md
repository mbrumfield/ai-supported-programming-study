
# Design Specification: Automated File System Deployment
**Company:** GT Yummy Ice Cream  
**Prepared By:** [Your Name / Consultant ID]
**Date:** 2026.11.17

---

## 1. Base Deployment Path
Define the root test directory where the automation scripts will build the file hierarchy inside your Linux virtual machine.
- **Root Directory Path:** `[/path/to/your/test_root]` *(Example: `/tmp/gt_yummy_data`)*

---

## 2. Directory Hierarchy & Access Control Matrix
For each department, list the directory, who has access, and the required permissions. *Note: Specify permissions using both the human-readable access terms (**Read, Write, Execute**) or the Linux octal permission numbers (e.g., `700`, `750`, `770`, `775`).*

- **`[Department_1] / [e.g., Executive]`** 
  - **Permissions:** `[e.g., 700]` (Breakdown: Owner has **Read, Write, Execute**; Group and Others have **No Access**)
  - **Description:** Strictly restricted to senior leadership.
  - **Subdirectories:**
    - `[Subfolder_A]` (Permissions: )
    - `[Subfolder_B]` (Permissions: )

- **`[Department_2] / [e.g., Accounting]`** 
  - **Permissions:** `[e.g., 750]` (Breakdown: Owner has **Read, Write, Execute**; Group has **Read and Execute**; Others have **No Access**)
  - **Description:** Restricted financial and invoice records.
  - **Subdirectories:**
    - `[Subfolder_A]` (Permissions: )
    - `[Subfolder_B]` (Permissions: )

- **`[Department_3] / [e.g., Marketing]`** 
  - **Permissions:** `[e.g., 750]` (Breakdown: Owner has **Read, Write, Execute**; Marketing group has **Read and Execute**)
  - **Description:** Campaign assets and distributor outreach materials.
  - **Subdirectories:**
    - `[Subfolder_A]` (Permissions: )

- **`[Department_4] / [e.g., Manufacturing]`** 
  - **Permissions:** `[e.g., 770]` (Breakdown: Owner and Operations group both have **Read, Write, Execute**; Others have **No Access**)
  - **Description:** Linux workstation inventory and production logs.
  - **Subdirectories:**
    - `[Subfolder_A]` (Permissions: )

- **`[Department_5] / [e.g., Shared]`** 
  - **Permissions:** `[e.g., 775]` (Breakdown: Owner and Group have **Read, Write, Execute**; Others have **Read and Execute**)
  - **Description:** Company-wide IT policies and resources accessible by all departments.
  - **Subdirectories:**
    - `[Subfolder_A]` (Permissions: )

---

## 3. File Naming Convention Rules
Specify the strict naming syntax that the LLM-generated scripts must use for all automatically created files.

---

## 4. Required Sample Files to Seed
List at least 3 sample files that the scripts must create across your directory tree, including their target path and initial placeholder text.

1. **Path:** `[Relative path to folder and file name]`
   - *Initial Content:* `[Text string to write into the file]`
2. **Path:** `[Relative path to folder and file name]`
   - *Initial Content:* `[Text string to write into the file]`
3. **Path:** `[Relative path to folder and file name]`
   - *Initial Content:* `[Text string to write into the file]`

Review rounds table

-------------------

  

| Round | Number of findings | Main changes made | Suggestions rejected with explanation |
| ----- | ----- | ----- | ----- | ----- | 
|1       |       |Changed...       |       |       |
|2 | | Changed... | I kept everything the same.|

## Implementation
Both the Bash script (`deploy_gt_yummy.sh`) and the Python script (`deploy_gt_yummy.py`) must adhere to the following operational standards:

### A. General Automation Rules
- **Idempotency:** The scripts must be safe to run multiple times without crashing or overwriting existing data (e.g., using `mkdir -p` in Bash or `exist_ok=True` in Python).
- **Status Logging:** The scripts must print clear, human-readable messages to the terminal as each folder, permission, and file is created (e.g., `[SUCCESS] Created directory: /tmp/gt_yummy_data/Accounting`).

### B. Bash Script Requirements (`deploy_gt_yummy.sh`)
- Must start with the standard shebang: `#!/bin/bash`
- Must apply octal permissions using `chmod` and `chmod -R` (recursive where appropriate).
- Must verify that the base root directory exists before building subdirectories.

### C. Python Script Requirements (`deploy_gt_yummy.py`)
- Must use built-in standard libraries (`os`, `pathlib`, and `datetime`) without requiring external pip packages.
- Must use `pathlib.Path` for safe, cross-platform path handling.
- Must apply permissions using `os.chmod()` with explicit octal values (e.g., `0o750`).
