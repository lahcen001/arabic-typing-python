#!/usr/bin/env python3

from yamliwrapper import Transliterator

def interactive_demo():
    print("=== Interactive Yamli API Demo ===")
    print("Enter English/Franco-Arabic text to get Arabic transliterations")
    print("Type 'quit' or 'exit' to stop")
    print()
    
    while True:
        try:
            user_input = input("Enter word to transliterate: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '']:
                print("Goodbye!")
                break
                
            print(f"Transliterating '{user_input}'...")
            transliterator = Transliterator(user_input)
            candidates = transliterator.candidates
            
            if candidates:
                print(f"Arabic candidates:")
                for i, candidate in enumerate(candidates[:5], 1):  # Show top 5
                    print(f"  {i}. {candidate}")
                print(f"Best match: {candidates[0]}")
            else:
                print("No candidates found. Try a single word without spaces.")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("-" * 40)

if __name__ == "__main__":
    interactive_demo() 