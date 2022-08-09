from lib.controllers import Controller
from lib.arguments import parse_args
import multiprocessing
import keep_alive

if __name__ == "__main__":
    keep_alive.keep_alive()
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args()
    )
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass