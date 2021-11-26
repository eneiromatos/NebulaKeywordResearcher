import config


class FileWriter:

    @staticmethod
    def write_txt(kws: tuple[str]):
        with open(config.output_file, mode='a') as kws_file:
            unique_kws = set(kws)
            for kw in unique_kws:
                if kw in ('', ' ', None):
                    continue
                kws_file.write(f'{kw}\n')
