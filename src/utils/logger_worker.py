import logging
from pathlib import Path


class LoggerWorker:
    """Класс для логирования работы приложения"""
    def __init__(
            self,
            log_dir: Path = Path(__file__).parent.parent.parent / "logs",
            log_file: str = "app.log",
            level: int = logging.INFO
    ) -> None:
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / log_file

        # Настраиваем логгер
        self.logger = logging.getLogger("VacancyObserverLogger")
        self.logger.setLevel(level)
        self.logger.propagate = False

        # Настраиваем форматтер
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Настраиваем хэндлер для логгирования в файл и в консоль
        if not self.logger.handlers:
            file_handler = logging.FileHandler(self.log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        """Метод для уровня логгирования DEBUG"""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Метод для уровня логгирования INFO"""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Метод для уровня логгирования WARNING"""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Метод для уровня логгирования ERROR"""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Метод для уровня логгирования CRITICAL"""
        self.logger.critical(message)
