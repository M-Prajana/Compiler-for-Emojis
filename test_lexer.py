# test_lexer.py — Full Lexer Test Suite for CWE-Compiler
from lexer import Lexer
from tokens import TokenType, TOKEN_MAP

def run_test(code, description=""):
    print(f"\n=== Test: {description} ===")
    print("Source Code:\n", code)
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("\nTokens:")
    unmapped = []
    for token in tokens:
        print(token)
        if token.type not in TOKEN_MAP.values() and token.type not in {v for v in vars(TokenType).values() if isinstance(v, str)}:
            unmapped.append(token)

    if unmapped:
        print("\n⚠️ Unmapped / Unknown Tokens Found:")
        for t in unmapped:
            print(t)
    else:
        print("\n✅ All tokens recognized.")
    print("=" * 60)

    return tokens, unmapped

def print_tokens(tokens):
    print(f"{'Type':<15} | {'Value':<15} | {'Line':<4} | {'Col':<4}")
    print("-" * 50)
    for t in tokens:
        value = t.value if t.value is not None else ""
        print(f"{t.type:<15} | {value:<15} | {t.line:<4} | {t.column:<4}")
    print("\n")

if __name__ == "__main__":
    tests = [
        ("Basic program + I/O + comment", '''
            👋 main() {
                🔤 msg = "Hello World!";
                📢 msg;
                ❓➕(5, 10);
                📝 This is a comment
            }
        '''),

        ("All literals (NUMBER, FLOAT, CHAR, STRING, NULL)", '''
            let a = 10;
            let b = 3.14;
            let c = 'X';
            let s = "Sample";
            let n = 🚫;
        '''),

        ("Operators, compound assignments, comparison", '''
            a += 5; b -= 2; c *= 3; d /= 4; e % 2; f ^ 3;
            a == b; a != b; a > b; a < b; a >= b; a <= b;
        '''),

        ("Boolean, logical, unary operators", '''
            ✅ x; ❌ y;
            x 🟰 y; x ⭕ y; ❎ z; ✖⭕ w;
            x 🔼+; y 🔽-;
        '''),

        ("Bitwise and shift operators", '''
            a & b; c | d; e ^ f; g << 2; h >> 3;
        '''),

        ("Conditionals, loops, break/continue, blocks", '''
            ❓(x > 0) { 📢 "Positive"; }
            🤔 { 📢 "Else block"; }
            ❓➕(x == 0) { 📢 "ElseIf block"; }
            🔁(i < 10) { i += 1; }
            🔂(i, 0, 5) { 📢 i; }
            🛑; ⏭;
            🔚
        '''),

        ("Arrays / lists operations", '''
            squad nums = [1,2,3];
            add2squad nums 4;
            peek nums 1;
            howlong nums;
        '''),

        ("Built-ins and throw/error handling", '''
            looprange 0, 5;
            ⚠ "Something went wrong!";
        '''),

        ("Function definition + return", '''
            🛠 vibe add(a, b) {
                🎁 a + b;
            }
        '''),

        ("Switch / Case / Default", '''
            🎚 switchup x {
                ➡️ 1 { 📢 "One"; }
                ➡️ 2 { 📢 "Two"; }
                🚪 { 📢 "Other"; }
            }
        '''),

        ("Input example", '''
            📥 name;
            📢 name;
        '''),

        ("Unknown token test", '''
            @ $ # ~;
        '''),

        ("Symbols and formatting tokens", '''
            ( ) { } ; , ? : . \\ 
        '''),
        ("Missing arithmetic and bitwise tokens", '''
            a + b; a ➕ b; a plus b;
            a - b; a ➖ b; a minus b;
            a * b; a ✖ b; a times b;
            a / b; a ➗ b; a div b;
            a ^^^ b;  # BIT_XOR
        '''),

        ("Full mixed program", '''
            👋 main() {
                🔤 a = "Test";
                let b = 42; 
                ✅ flag; 
                📢 a; 
                ❓(b > 0) { 📢 "Positive"; }
                🤔 { 📢 "Negative"; }
                🔁(i < 5) { i += 1; }
                squad lst = [1,2,3];
                add2squad lst 4;
                peek lst 2;
                howlong lst;
                🛠 vibe multiply(x, y) { 🎁 x * y; }
                🔚
            }
        '''),
    ]

    all_tokens = []
    all_unmapped = []

    for desc, code in tests:
        tokens, unmapped = run_test(code, desc)
        all_tokens.extend(tokens)
        all_unmapped.extend(unmapped)

    # ✅ Coverage check (only actual TokenType strings)
    required_types = {
        getattr(TokenType, attr)
        for attr in dir(TokenType)
        if not attr.startswith("__") and isinstance(getattr(TokenType, attr), str)
    }
    covered_types = {t.type for t in all_tokens}

    missing = required_types - covered_types

    print("\n=== Coverage Summary ===")
    print(f"✅ Covered: {len(covered_types)} / {len(required_types)} TokenTypes")
    if missing:
        print("⚠️ Missing:", missing)
    if all_unmapped:
        print("⚠️ Unknown tokens found:", all_unmapped)
    else:
        print("✅ No unknown tokens found.")

    # 🔥 Assertions for CI / automated testing
    assert not missing, f"Missing TokenTypes: {missing}"
    assert not all_unmapped, f"Unknown tokens encountered: {all_unmapped}"
    print("\n🎉 Lexer passed all tests with full coverage!")
