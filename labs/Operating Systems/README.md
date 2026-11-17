Lab: Automated File System Deployment \& Infrastructure Scripting
=================================================================

Overview
--------

In our previous Case Study, you acted as an IT consultant for **GT Yummy Ice
Cream**, designing a file hierarchy to support a mixed-OS environment (macOS for
Senior Management, Windows 10 for Marketing and Accounting, and Linux for
Manufacturing/Operations) backed by central file servers.

In modern IT operations, administrators rarely build large directory structures
or configure permissions manually. Instead, they write **Design Specifications**
and use automation scripts (Bash and Python) to deploy infrastructure reliably
and repeatably.

In this lab, you will formalize your GT Yummy Ice Cream file structure into a
Markdown Design Specification, use an LLM (large language model) to generate
Bash and Python scripts from that specification, and test both deployments in
your virtual machine environment.

---

Learning Objectives
-------------------

By the end of this lab, you will be able to:

1. Translate a conceptual enterprise file hierarchy and access-control plan into
   a structured **Markdown Design Specification**.
2. Leverage an LLM to generate system administration scripts in **Bash** and
   **Python** using precise technical prompting.
3. Implement directory creation, file naming conventions, and Linux file
   permissions (`chmod` / `chown`) programmatically.
4. Validate and audit automated deployments inside a Linux virtual machine
   (Ubuntu/Mint).

---

Scenario Context: GT Yummy Ice Cream
------------------------------------

Recall your consulting brief:

* <strong>Senior Management (President \& VPs):</strong> Uses macOS; requires
  confidential access to executive strategy and company-wide financials.
* <strong>Marketing Department:</strong> Uses Windows 10; requires shared access
  to campaigns, branding assets, and distributor outreach.
* <strong>Accounting Department:</strong> Uses Windows 10; requires restricted
  access to budgets, payroll, and distributor invoices.
* <strong>Manufacturing \& Operations:</strong> Uses Linux workstations;
  requires access to production schedules, inventory logs, and quality control
  records.
* <strong>Public/Company-Wide:</strong> All departments need a shared read/write
  dropbox or general resources folder.

---

Instructions
------------

### Part 1: Create the Markdown Design Specification

Create a file named `design_spec.md`. This document will serve as the single
source of truth that you feed to an LLM. Your specification must include:

1. <strong>Root Directory:</strong> A clear base path for testing in your VM
   (e.g., `/tmp/gt_yummy_test` or `~/gt_yummy_data`).
2. <strong>Departmental Hierarchy:</strong> Subdirectories for Executive,
   Marketing, Accounting, Manufacturing, and Shared. Include at least two
   sub-folders inside each department.
3. <strong>Access Control \& Permissions Matrix:</strong> Define Linux octal
   permissions (e.g., `750`, `770`, `775`) for each directory based on the
   principle of least privilege (e.g., Accounting and Executive folders must not
   be readable by general users).
4. <strong>File Naming Convention \& Sample Files:</strong> Define a strict
   date-prefixed naming convention (`YYYY.MM.DD_Department_DocumentName.txt`,
   e.g., `2026.01.20_Accounting_Q1Budget.txt`) and list at least 5 sample files
   to be automatically generated across the folders.

### Part 2: Refine the Design Spec \& Generate the Bash Script

Provide your `design_spec.md` to Copilot (via your `my.tougaloo.edu` account) or
Gemini, and ask it to evaluate and provide suggestions to improve your document
(e.g., <em>"Review this specification"</em>). Don't adopt every suggestion;
decide which suggestions are relevant.

Record the review round, how many findings Copilot or Gemini identified, and a
short, one-sentence summary of the changes you made in the review rounds table
below:

| Round | Number of Findings | Main Changes Made                                     | Suggestions Rejected with Explanation                     |
| ----- | ------------------ | ----------------------------------------------------- | --------------------------------------------------------- |
| 1     | 3                  | Improved directory permissions for executive folders. | Rejected public group read access due to confidentiality. |
| 2     | ...                | ...                                                   | ...                                                       |

Repeat this process until the problems identified are trivial or contradictory.
After you are satisfied with your design spec, instruct Copilot or Gemini to
generate a Bash script (`deploy_gt_yummy.sh`) that builds the environment (e.g.,
<em>"Implement this specification as a Linux Bash script"</em>).

### Part 3: Generate \& Refine the Python Script

Using the same `design_spec.md`, prompt the LLM to generate a Python 3 script
(`deploy_gt_yummy.py`) that accomplishes the exact same deployment, targeting a
separate test root (e.g., `~/gt_yummy_python_test`) so you can compare them
side-by-side.

### Part 4: Execute and Audit the Scripts

Boot up your Linux VM (Ubuntu or Linux Mint) and perform the following:

* <strong>Bash Script Execution:</strong>

  ```bash
  chmod +x deploy_gt_yummy.sh
  ./deploy_gt_yummy.sh
  ```

* <strong>Python Script Execution:</strong>

```python
python3 deploy_gt_yummy.py
```

### Part 5: Reflection

Write a paragraph about what you learned from this assignment and your thoughts
overall.

### Submission

Submit your design specification document (`design_spec.md`), your automation
scripts (`deploy_gt_yummy.sh`, `deploy_gt_yummy.py`), and your reflection
response from Part 5.
