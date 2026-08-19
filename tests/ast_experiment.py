import ast


code = """
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
"""


tree = ast.parse(code)

print(ast.dump(tree, indent=4))