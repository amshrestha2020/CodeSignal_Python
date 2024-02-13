from urllib.parse import urlparse, parse_qs

def solution(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)

    similarity = 0

    # +5, if the same protocol is used in both URLs.
    if parsed_url1.scheme == parsed_url2.scheme:
        similarity += 5

    # +10, if url1 and url2 have the same address.
    if parsed_url1.netloc == parsed_url2.netloc:
        similarity += 10

    # +k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
    path1 = parsed_url1.path.split('/')[1:]  # Ignore the first empty string before the first '/'
    path2 = parsed_url2.path.split('/')[1:]  # Ignore the first empty string before the first '/'
    similarity += sum(1 for p1, p2 in zip(path1, path2) if p1 == p2)

    # +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
    query1 = parse_qs(parsed_url1.query)
    query2 = parse_qs(parsed_url2.query)
    common_keys = set(query1.keys()) & set(query2.keys())
    similarity += len(common_keys)
    similarity += sum(1 for key in common_keys if query1[key] == query2[key])

    return similarity
