**Admin Prompt for SAST Scanning**

**Objective:**
Perform a comprehensive Static Application Security Testing (SAST) scan on the provided source code to identify potential vulnerabilities, coding errors, and security weaknesses.

**Scan Requirements:**
1. **Scope of Scan:**
   - Include all directories and subdirectories within the project repository.
   - Ensure all source files and configurations (e.g., `.env` files, Docker configurations) are included in the scan.

2. **Vulnerability Categories to Focus On:**
   - Injection Flaws (SQL, Command, LDAP, XPath, etc.)
   - Cross-Site Scripting (XSS)
   - Insecure Cryptographic Storage
   - Security Misconfiguration
   - Sensitive Data Exposure
   - Broken Authentication and Session Management
   - Cross-Site Request Forgery (CSRF)
   - Insufficient Logging and Monitoring
   - Server-Side Request Forgery (SSRF)

3. **Compliance Standards:**
   - OWASP Top 10
   - CWE/SANS Top 25
   - PCI-DSS (if applicable)
   - GDPR (if applicable)
   - HIPAA (if applicable)

4. **Output Requirements:**
   - Detailed report of identified vulnerabilities with descriptions, severity levels (e.g., High, Medium, Low), and suggested remediation steps.
   - Summary of findings including the total number of vulnerabilities detected.
   - Metrics on code quality and security posture.

**Additional Configuration:**
- Specify any third-party libraries or dependencies that need to be included in the scan.
- Define exclusions (if any) for certain files or directories that should not be scanned.
- Identify any custom rules or company-specific coding standards that need to be enforced during the scan.

**Post-Scan Actions:**
1. **Report Delivery:**
   - Deliver a comprehensive report in both PDF and machine-readable formats (e.g., JSON).
   - Provide access to an interactive dashboard for visualizing the scan results.

2. **Notifications:**
   - Send email notifications to the security team with a summary of the scan results and a link to the detailed report and dashboard.
   - Provide automated alerts for critical vulnerabilities.

3. **Remediation Follow-Up:**
   - Schedule a follow-up session with the development team to discuss and prioritize the remediation of identified issues.
   - Offer support for patching critical vulnerabilities immediately.

**Access and Permissions:**
- Ensure the AI has read-only access to the source code repository and necessary configurations.
- Grant administrative access to generate reports and notifications.

