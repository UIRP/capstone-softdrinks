import pandas

def combine(entry):
    '''
    Assess closeness based on customer and rating.

    Notably, we omit description and classification.  This also
    spuriously associates customers with similar IDs, which is
    basically voodoo.
    '''
    return f"{entry['Customer_id']} {entry['Rating']}"


class holden:
    def __init__(self):
        self.df = None
        self.cosine_sim = None

    def get_item_from_id(self,id):
        return self.df[self.df['Item_id'] == id]['Item_Description'].iloc[0]
    def get_id_from_item(self,item):
        return self.df[self.df['Item_Description'] == item]['Item_id'].iloc[0]

    def get_index_from_id(id):
        return self.df[self.df['Item_id'] == id].index[0]
    def get_item_from_index(index):
        return self.df[self.df.index == index]['Item_Description'].iloc[0]

    def initialize(self,df):
        self.df = df.copy()
        
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        features = ['Customer_id','Rating','Item_Description']

        for feature in features:
            self.df[feature] = self.df[feature].fillna('')

        self.df['Combined'] = self.df.apply(combine,axis=1)

        cv = CountVectorizer()
        count_matrix = cv.fit_transform(selfdf['Combined'])
        
        self.cosine_sim = cosine_similarity(count_matrix)
    
    def match(self,item):
        item_index = self,get_index_from_id(self.get_id_from_item(item))
        similar_soft_drinks = list(enumerate(cosine_sim[item_index]))
        similar_sorted = sorted(similar_soft_drinks,key=lambda x:x[1],reverse=True)[1:]

        best_matches = []
        for i in range(0,5):
            try:
                best_matches.append(self.get_item_from_index(similar_sorted[i][0]))
            except IndexError:
                print('Empty DF')
                continue

