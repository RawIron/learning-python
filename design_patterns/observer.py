
class Observer(object):
    def update(self, event):
        raise NotImplementedError

class Observable(object):
    def __init__(self):
        self.subscribers = []
    def subscribe(self, o):
        self.subscribers.append(o)
    def unsubscribe(self, o):
        self.subscribers.remove(o)
    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.update(event)


class Achievement(object):
    def __init__(self):
        self.threshold = 10
        self.counter = 0
        self.level = 1
    def update(self, event):
        self.counter += event
        if self.is_earned():
            self.level += 1
    def is_earned(self):
        if self.counter > self.threshold:
            return True
        else:
            return False

class Gun(Observable):
    def __init__(self):
        super(Gun, self).__init__()
        self.munition = 3

    def loaded(self):
        return (self.munition > 0)

    def fire(self):
        if not self.loaded:
            return
        self.munition -= 1
        self.notify(9)

