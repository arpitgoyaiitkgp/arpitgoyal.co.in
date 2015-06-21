class MyPersonalDetails(object):

    def __init__(self):
        self.about = self.get_about_string()
        self.experience = self.get_experience_details()

    def get_about_string(self):

        ABOUT = '''Hi, my name is Arpit Goyal and I specialize in Electrical Engineering from Indian Institute of Technology Kharagpur. Now I work as Software Developer at HT Media Ltd. I love working with passionate people and sharing what I've learned with them. This website is my window to the world where you can find more about me and then get in touch for a chat about potential projects.'''

        return ABOUT

    def get_experience_details(self):
        pass
