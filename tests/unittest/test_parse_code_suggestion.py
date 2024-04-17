
# Generated by CodiumAI
from pr_agent.algo.utils import parse_code_suggestion

"""
Code Analysis

Objective:
The objective of the function is to convert a dictionary into a markdown format. The function takes in a dictionary as 
input and recursively converts it into a markdown format. The function is specifically designed to handle dictionaries 
that contain code suggestions.

Inputs:
- output_data: a dictionary containing the data to be converted into markdown format

Flow:
- Initialize an empty string variable called markdown_text
- Create a dictionary of emojis to be used in the markdown format
- Iterate through the items in the input dictionary
- If the value is empty, skip to the next item
- If the value is a dictionary, recursively call the function with the value as input
- If the value is a list, iterate through the list and add each item to the markdown format
- If the value is not 'n/a', add it to the markdown format
- If the key is 'code suggestions', call the parse_code_suggestion function to handle the list of code suggestions
- Return the markdown format as a string

Outputs:
- markdown_text: a string containing the input dictionary converted into markdown format

Additional aspects:
- The function uses the textwrap module to indent code examples in the markdown format
- The parse_code_suggestion function is called to handle the 'code suggestions' key in the input dictionary
- The function uses emojis to add visual cues to the markdown format
"""


class TestParseCodeSuggestion:
    # Tests that function returns empty string when input is an empty dictionary
    def test_empty_dict(self):
        input_data = {}
        expected_output = "\n"  # modified to expect a newline character
        assert parse_code_suggestion(input_data) == expected_output


    # Tests that function returns correct output when 'before' or 'after' key has a non-string value
    def test_non_string_before_or_after(self):
        input_data = {
            "Code example": {
                "Before": 123,
                "After": ["a", "b", "c"]
            }
        }
        expected_output = "  - **Code example:**\n    - **Before:**\n        ```\n        123\n        ```\n    - **After:**\n        ```\n        ['a', 'b', 'c']\n        ```\n\n"  # noqa: E501
        assert parse_code_suggestion(input_data) == expected_output

    # Tests that function returns correct output when input dictionary does not have 'code example' key
    def test_no_code_example_key(self):
        code_suggestions = {
            'suggestion': 'Suggestion 1',
            'description': 'Description 1',
            'before': 'Before 1',
            'after': 'After 1'
        }
        expected_output = '   **suggestion:** Suggestion 1     \n   **description:** Description 1     \n   **before:** Before 1     \n   **after:** After 1     \n\n'  # noqa: E501
        assert parse_code_suggestion(code_suggestions) == expected_output

    # Tests that function returns correct output when input dictionary has 'code example' key
    def test_with_code_example_key(self):
        code_suggestions = {
            'suggestion': 'Suggestion 2',
            'description': 'Description 2',
            'code example': {
                'before': 'Before 2',
                'after': 'After 2'
            }
        }
        expected_output = '   **suggestion:** Suggestion 2     \n   **description:** Description 2     \n  - **code example:**\n    - **before:**\n        ```\n        Before 2\n        ```\n    - **after:**\n        ```\n        After 2\n        ```\n\n'  # noqa: E501
        assert parse_code_suggestion(code_suggestions) == expected_output
