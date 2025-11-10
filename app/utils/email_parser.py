from bs4 import BeautifulSoup

def parse_email(html_content: str) -> str:
    """
    Convert HTML email body to readable text.
    Removes tags, newlines, and common signatures.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")

    # Clean excessive whitespace
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean_text = "\n".join(lines)

    # Remove common signature markers
    if "--" in clean_text:
        clean_text = clean_text.split("--")[0]

    return clean_text
