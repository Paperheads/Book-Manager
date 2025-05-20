from cli import BookCLI

def main():
    cli = BookCLI("books.json")
    cli.run()

if __name__ == "__main__":
    main()
