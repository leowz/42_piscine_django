class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name;

    def __str__(self):
        return (self.name);

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...");
    
    def make_coffee(self):
        return self.Coffee();

    class Coffee:
        def __init__(self, name="expresso"):
            self.name = name;

        def __str__(self):
            return "This is coffee {}".format(self.name);


if __name__ == '__main__':
    it1 = Intern();
    it2 = Intern("Mark");
    print(it1);
    print(it2);
    print(str(it2.make_coffee()) + " by " + str(it2));

    try:
        it1.work();
    except Exception as e:
        print(e);
