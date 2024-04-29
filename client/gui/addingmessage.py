class AddingMesssage:
    
    def __init__(self):
        self.location = ""
        self.delay = 0
        self.message = ""
        self.keywords = []
    
    def get_gui_data(self, message, keywords):
        dataMessage = message
        dataKeywords = keywords
        
        print("This is the information {0}, {1}".format(dataMessage, dataKeywords))
        
    
    
    def submit_message(self, message):
        self.message = message
    
    def submit_key_word(self, keyword):
        self.keywords.append(keyword)
    
    def show_all_keyword(self):
        return self.keywords
    
    
        
        

