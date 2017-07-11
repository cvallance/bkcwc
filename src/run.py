from junitparser import JUnitXml
from html import escape
import os
import config

test_file_path = os.path.join(config.TEST_FILE_DIRECTORY, config.TEST_FILE_NAME)
if not os.path.exists(test_file_path):
    print(f'<h4>ERROR Running bkcwc</h4>\n\nCould not find the test file "{test_file_path}"')
    exit(1)

suite = JUnitXml.fromfile(test_file_path)
passed_tests = suite.tests - suite.failures - suite.errors - suite.skipped

has_error = False
if suite.failures or suite.errors:
    has_error = True

title = 'Tests Passed!' if not has_error else 'Tests Failed!'
print(f'<h4>{title}</h4>\n')
print('<span>')
print(f'Total Tests: {suite.tests} | Passed: {passed_tests} | Skipped: {suite.skipped} | '
      f'Failures: {suite.failures} | Errors: {suite.errors}')
print('</span>')

if has_error:
    for i, case in enumerate(suite):
        result = case.result
        if not result or result._elem.tag not in ['failure', 'error']:
            continue

        print('<details>')
        print(f'<summary><code>{result._elem.tag.upper()}: {case.name} in {case.classname}</code></summary>')
        print('<code><pre>')
        print(f'{result._elem.text}')
        print('</pre></code>')
        print('</details>\n')

exit(1 if has_error else 0)
