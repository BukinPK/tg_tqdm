import telegram.ext
from tqdm import tqdm
from datetime import datetime


class _TelegramIO:
    def __init__(self, token, chat_id, show_last_update=True, parse_mode=None):
        self.updater = telegram.ext.Updater(token=token, use_context=True,
                                            defaults=telegram.ext.Defaults(parse_mode=parse_mode))
        self.chat_id = chat_id
        self.parse_mode = parse_mode
        self.text = self.prev_text = '[init tg_tqdm bar]'
        self.message_id = self.updater.bot.send_message(chat_id, self.text)['message_id']
        self.show_last_update = show_last_update

    def write(self, s):
        new_text = s.strip().replace('\r', '').replace('[A', '')
        if new_text:
            self.text = new_text

    def flush(self):
        if self.prev_text != self.text:
            text = self.text + f'\nLast update: {datetime.now()}' if self.show_last_update else self.text
            self.updater.bot.edit_message_text(text, self.chat_id, self.message_id)
            self.prev_text = self.text


class TgTqdm:

    def __init__(self, token, chat_id, show_last_update=False, parse_mode=None,
                 **kwargs):
        """
        Decorate an iterable object, returning an iterator which acts exactly
        like the original iterable, but send to Telegram a dynamically updating
        progressbar every time a value is requested.

            Parameters
            ----------
            parse_mode  : HTML or MARKUP

            iterable  : iterable, required
                Iterable to decorate with a progressbar.
                Leave blank to manually manage the updates.
            token  : string, required
                Token of your telegram bot

            chat_id  : int, required
                Chat ID where information will be sent about the progress

            show_last_update  : bool, optional [default: True]
                Should I show the time-date of the last change in the progress bar?

            desc, total, leave, ncols, ... :
                Like in tqdm

        """
        self.tg_io = _TelegramIO(token, chat_id, show_last_update, parse_mode)
        self.kwargs = kwargs

    def __call__(self, iterable, **kwargs):
        kwargs = {**self.kwargs, **kwargs}
        return tqdm(iterable=iterable, file=self.tg_io, **kwargs)


def tg_tqdm(iterable, token, chat_id, show_last_update=False, parse_mode=None,
            **kwargs):
    return TgTqdm(token, chat_id, show_last_update, parse_mode,
                  **kwargs)(iterable)
