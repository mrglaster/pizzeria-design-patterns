from pathlib import Path


class BannerPrinter:

    @staticmethod
    def print_banner():
        with open(f'{Path(__file__).parent.resolve()}/banner.txt') as f:
            lines = f.readlines()
            for i in lines:
                print(i.replace('\n', ''))
        print()
