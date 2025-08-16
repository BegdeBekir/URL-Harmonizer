import argparse

def url_harmonizer(input_list):
    """
    Generates both HTTP and HTTPS links for a given list of URLs or domains.
    Creates new versions even if inputs already have a protocol.

    Args:
        input_list: A list of URLs or domains (e.g., ["google.com", "http://example.org"]).

    Returns:
        A list containing both HTTP and HTTPS versions for each input.
    """
    full_url_list = []
    for entry in input_list:
        entry = entry.strip()  # boşluk/bozuklukları temizle
        if not entry:
            continue

        # Clean up the protocol (if it exists)
        if entry.startswith("http://"):
            cleaned_domain = entry.replace("http://", "")
        elif entry.startswith("https://"):
            cleaned_domain = entry.replace("https://", "")
        else:
            cleaned_domain = entry

        # Add both HTTP and HTTPS versions
        full_url_list.append(f"http://{cleaned_domain}")
        full_url_list.append(f"https://{cleaned_domain}")
    return full_url_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="URL Harmonizer - Create HTTP & HTTPS versions of URLs.")
    parser.add_argument("--input", required=True, help="Input file path containing list of URLs/domains")
    parser.add_argument("--output", required=True, help="Output file path to save generated links")

    args = parser.parse_args()

    # input.txt içeriğini oku
    with open(args.input, "r", encoding="utf-8") as f:
        urls = f.readlines()

    # URL'leri harmonize et
    generated_links = url_harmonizer(urls)

    # output.txt dosyasına yaz
    with open(args.output, "w", encoding="utf-8") as f:
        for url in generated_links:
            f.write(url + "\n")

    print(f"✅ İşlem tamamlandı! Sonuçlar '{args.output}' dosyasına kaydedildi.")
