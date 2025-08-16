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
        # Clean up the protocol (if it exists)
        if "http://" in entry:
            cleaned_domain = entry.replace("http://", "")
        elif "https://" in entry:
            cleaned_domain = entry.replace("https://", "")
        else:
            cleaned_domain = entry

        # Add both HTTP and HTTPS versions
        full_url_list.append(f"http://{cleaned_domain}")
        full_url_list.append(f"https://{cleaned_domain}")
    return full_url_list

# Example usage:
# You can mix domains and full URLs here
my_inputs = ["example.com", "http://google.com", "https://yandex.ru", "medium.com"]

generated_links = url_harmonizer(my_inputs)

for url in generated_links:
    print(url)
