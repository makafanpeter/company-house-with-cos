class Company:
    def __init__(self,
                 name,
                 address,
                 city,
                 county, post_code,
                 type_and_rating, route):
        self.name = name
        self.address = address
        self.city = city
        self.state = county
        self.post_code = post_code
        self.type_and_rating = type_and_rating
        self.route = route
