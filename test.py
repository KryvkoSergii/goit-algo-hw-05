
import timeit
import kmp
import boyer_moore
import rabin_karp

def time_search_algorithm(algorithm, content, to_find):
    return timeit.timeit(lambda: algorithm(content, to_find), number=100)

def main():
    file_path_1 = './data/article_1.txt'
    file_path_2 = './data/article_2.txt'

    with open(file_path_1, 'r', encoding="utf-8") as file:
        content1 = file.read()
    with open(file_path_2, 'r', encoding="utf-8") as file:
        content2 = file.read()

    substring_to_find_1 = content1[400:420]
    substring_to_find_2 = content2[600:620]
    fake_substring = "some-unknown"


    print(f"========= Test =========")

    print(f"KMP, article 1: {time_search_algorithm(kmp.kmp_search, content1, substring_to_find_1)}")
    print(f"KMP, article 2: {time_search_algorithm(kmp.kmp_search, content2, substring_to_find_2)}")
    print(f"KMP, article 1 (unknown) : {time_search_algorithm(kmp.kmp_search, content1, fake_substring)}")
    print(f"KMP, article 1 (unknown) : {time_search_algorithm(kmp.kmp_search, content2, fake_substring)}")

    print(f"boyer moore, article 1: {time_search_algorithm(boyer_moore.boyer_moore_search, content1, substring_to_find_1)}")
    print(f"boyer moore, article 2: {time_search_algorithm(boyer_moore.boyer_moore_search, content2, substring_to_find_2)}")
    print(f"boyer moore, article 1 (unknown): {time_search_algorithm(boyer_moore.boyer_moore_search, content1, fake_substring)}")
    print(f"boyer moore, article 2 (unknown): {time_search_algorithm(boyer_moore.boyer_moore_search, content2, fake_substring)}")

    print(f"rabin karp, article 1: {time_search_algorithm(rabin_karp.rabin_karp_search, content1, substring_to_find_1)}")
    print(f"rabin karp, article 2: {time_search_algorithm(rabin_karp.rabin_karp_search, content2, substring_to_find_2)}")
    print(f"rabin karp, article 1 (unknown): {time_search_algorithm(rabin_karp.rabin_karp_search, content1, fake_substring)}")
    print(f"rabin karp, article 2 (unknown): {time_search_algorithm(rabin_karp.rabin_karp_search, content2, fake_substring)}")

if __name__ == "__main__":
    main()