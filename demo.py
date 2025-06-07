xt#!/usr/bin/env python3

from yamliwrapper import Transliterator

def main():
    print("=== Yamli API Demo ===")
    print("This demo shows how to use the yamli-api to transliterate English text to Arabic")
    print()
    
    # Test cases
    test_words = ["salam", "ahlan", "7abibi", "shukran", "mabrook"]
    
    for word in test_words:
        print(f"Testing with '{word}':")
        try:
            transliterator = Transliterator(word)
            candidates = transliterator.candidates
            
            if candidates:
                print(f"  Arabic candidates: {candidates}")
                print(f"  Best match: {candidates[0]}")
            else:
                print("  No candidates found")
        except Exception as e:
            print(f"  Error: {e}")
        print()

if __name__ == "__main__":
    main() 