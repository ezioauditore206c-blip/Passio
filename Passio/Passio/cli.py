import argparse
from Passio import Passio
def main():
    parser = argparse.ArgumentParser(description="Passio CLI")
    subparsers = parser.add_subparsers(dest="command")

    gen = subparsers.add_parser("generate")
    gen.add_argument("--length", type=int, default=12)
    strength = subparsers.add_parser("strength")
    strength.add_argument("password")


    feedback = subparsers.add_parser("feedback")
    feedback.add_argument("password")

    args = parser.parse_args()
    p = Passio()

    if args.command == "generate":
        print(p.generate_password(args.length))
    elif args.command == "strength":
        print(p.password_strength(args.password))
    elif args.command == "feedback":
        print(p.feedback_tips(args.password))


if __name__ == "__main__":
    main()
