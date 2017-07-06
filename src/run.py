from junitparser import JUnitXml
from html import escape
import os
import config

test_file_path = os.path.join(config.TEST_FILE_DIRECTORY, config.TEST_FILE_NAME)
if not os.path.exists(test_file_path):
    print(f'Could not find the test file "{test_file_path}"')
    exit(1)

suite = JUnitXml.fromfile(test_file_path)
passed_tests = suite.tests - suite.failures - suite.errors - suite.skipped

has_error = False
if suite.failures or suite.errors:
    has_error = True

title = 'Tests Passed!' if not has_error else 'Tests Failed!'
print(f'<h3>{title}</h3>')
print(f'<span>'
      f'Total Tests: {suite.tests} | Passed: {passed_tests} | Skipped: {suite.skipped} | '
      f'Failures: {suite.failures} | Errors: {suite.errors}'
      f'</span>')

if has_error:
    for i, case in enumerate(suite):
        # print(f'{i} {case.classnamne} {case.name}')
        pass

exit(1 if has_error else 0)
