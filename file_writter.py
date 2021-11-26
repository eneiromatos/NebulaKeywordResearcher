import config
import time


class FileWriter:

    @staticmethod
    def write_txt(kws: tuple[str]):
        with open(config.output_file, mode='a', encoding='utf-8') as kws_file:
            unique_kws = set(kws)
            ord_kws = [f'{kw}\n' for kw in unique_kws]
            ord_kws.sort()
            kws_file.writelines(ord_kws)

    @staticmethod
    def write_log(error: str):
        with open(config.log_file, mode='a') as log:
            log.write(f'{time.ctime(time.time())}:\n'
                      f'Error: {error}\n\n')
