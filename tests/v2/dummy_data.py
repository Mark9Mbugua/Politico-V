party = {
        "party_name": "Jubilee",
        "hqAddress": "Muthaiga",
        "logoUrl": 'https://www.jubilee.com/jubilee/img.jpg'
}

same_party = {
        "party_name": "Jubilee",
        "hqAddress": "Muthaiga",
        "logoUrl": 'https://www.jubilee.com/jubilee/img.jpg'
}

office = {
    'office_type' : "Legislative",
    'office_name': "Member of Parliament",
    'location': "Kiambaa"
}

register = {
    "office": 1,
    "party": 1,
    "candidate": 1
}

vote = {
    "createdon": "2019-03-11 15:29:22.953523",
    "office": 1,
    "voter": 1,
    "candidate": 1
}

party_less_keys = {
    "party_name": "Jubilee",
    "hqAddress" : "Kinangop"
}

edit_party_no_name_key = {}

party_name_not_purely_alpha_and_space = {
    "party_name" : "Jubilee106",
    "hqAddress": "Muthaiga",
    "logoUrl": 'https://www.jubilee.com/jubilee/img.jpg'
}

office_less_keys = {
    "office_name": "Legislative"
}

party_name_blank = {
    "party_name": "",
    "hqAddress" : "Kinangop",
    "logoUrl" : "https://www.jubilee.com/jubilee/img.jpg" 
}

hqAddress_blank = {
    "party_name": "Jubilee",
    "hqAddress" : "",
    "logoUrl" : "https://www.jubilee.com/jubilee/img.jpg" 
}

logoUrl_blank = {
    "party_name": "Jubilee",
    "hqAddress" : "Muthaiga North",
    "logoUrl" : "" 
}

party_name_space = {
    "party_name": " ",
    "hqAddress" : "Kinangop",
    "logoUrl" : "https://www.twitter.com/profile/img.jpg"  
}

hqAddress_space = {
    "party_name": "Jubilee",
    "hqAddress" : " ",
    "logoUrl" : "https://www.twitter.com/profile/img.jpg" 
}

logoUrl_space = {
    "party_name": "Jubilee",
    "hqAddress" : "Muthaiga North",
    "logoUrl" : " " 
}
logoUrl_no_scheme = {
   "party_name": "The Northerners",
    "hqAddress" : "Winterfell",
    "logoUrl" : "//www.twitter.com/profile_pic.jpg"  
}

logoUrl_no_netloc = {
   "party_name": "Nasa ODM",
    "hqAddress" : "Ngong Road",
    "logoUrl" : "https:/profile_pic.jpg"  
}

logoUrl_no_path = {
   "party_name": "Ile Flani ya Wetangula",
    "hqAddress" : "Kwa Bibi yake",
    "logoUrl" : "https://www.twitter.com"  
}
hq_add_not_spaces_int_str = {
    "party_name": "Jubilee",
    "hqAddress" : "....",
    "logoUrl" : "https://www.twitter.com/profile/img.jpg'"  
}

hq_add_no_str = {
    "party_name": "Jubilee",
    "hqAddress" : "106106",
    "logoUrl" : "https://www.twitter.com/profile/img.jpg'" 
}

office_type_blank = {
    "office_type" : "",
    "office_name" : "President",
    "location": "Kenya"
}

office_name_blank = {
    "office_type" : "Executive",
    "office_name" : "",
    "location": "Kenya"
}

location_blank = {
    "office_type" : "Executive",
    "office_name" : "President",
    "location": ""
}

office_type_space = {
    "office_type" : " ",
    "office_name" : "President",
    "location": "Kenya"
}

office_name_space = {
    "office_type" : "Executive",
    "office_name" : " ",
    "location": "Kenya"
}

location_space = {
    "office_type" : "Executive",
    "office_name" : "President",
    "location": " "
}

office_type_not_string = {
	"office_type": 106,
	"office_name" : "MCA",
	"location": "Marurui"
}

office_name_not_string = {
	"office_type": "County",
	"office_name" : 106,
	"location": "Marurui"
}
location_not_string = {
	"office_type": "County",
	"office_name" : "MCA",
	"location": 106
}

office_type_not_letters = {
	"office_type": "County 106",
	"office_name" : "MCA",
	"location": "Marurui"
}

office_name_not_letters = {
	"office_type": "County",
	"office_name" : "MCA 106",
	"location": "Marurui"
}

location_not_letters = {
	"office_type": "County",
	"office_name" : "MCA",
	"location": "Marurui 106"
}

invalid_office_type = {
    "office_type" : "Cabinet",
    "office_name" : "President",
    "location" : "Kenya"
}

legislative_mismatch_president = {
    "office_type" : "Legislative",
    "office_name" : "President",
    "location" : "Kiambu Town"
}

legislative_mismatch_prime_minister = {
    "office_type" : "Legislative",
    "office_name" : "Prime Minister",
    "location" : "Kiambu Town"
}

legislative_mismatch_governor = {
    "office_type" : "Legislative",
    "office_name" : "Governor",
    "location" : "Kiambu Town"
}

legislative_mismatch_mca = {
    "office_type" : "Legislative",
    "office_name" : "MCA",
    "location" : "Kiambu Town"
}

executive_mismatch_governor = {
    "office_type" : "Executive",
    "office_name" : "Governor",
    "location" : "Kenya"
}

executive_mismatch_senator = {
    "office_type" : "Executive",
    "office_name" : "Senator",
    "location" : "Kenya"
}

executive_mismatch_mp = {
    "office_type" : "Executive",
    "office_name" : "Member of Parliament",
    "location" : "Kenya"
}

executive_mismatch_women_rep = {
    "office_type" : "Executive",
    "office_name" : "Women Rep",
    "location" : "Kenya"
}

executive_mismatch_mca = {
    "office_type" : "Executive",
    "office_name" : "MCA",
    "location" : "Kenya"
}

county_mismatch_president = {
    "office_type" : "County",
    "office_name" : "President",
    "location" : "Kiambu"
}

county_mismatch_prime_minister = {
    "office_type" : "County",
    "office_name" : "Prime Minister",
    "location" : "Kiambu"
}

county_mismatch_senator = {
    "office_type" : "County",
    "office_name" : "Senator",
    "location" : "Kiambu"
}

county_mismatch_mp = {
    "office_type" : "County",
    "office_name" : "Member of Parliament",
    "location" : "Kiambu"
}

county_mismatch_women_rep = {
    "office_type" : "County",
    "office_name" : "Women Rep",
    "location" : "Kiambu"
}

president_location_not_kenya = {
	"office_type": "Executive",
	"office_name" : "President",
	"location": "Uganda"
}

prime_min_location_not_kenya = {
	"office_type": "Executive",
	"office_name" : "Prime Minister",
	"location": "Uganda"
}

user_sign_up = {
	"firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Macabee106"
}

user_less_keys = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
}

pwd_less_char = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Mac1"
}

pwd_no_caps = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "markize106"
}

pwd_all_caps = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "MARKIZE106"
}

pwd_no_digit = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Markizeman"
}

firstname_all_char = {
    "firstname": "De*7#@",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Markize106"
}

lastname_all_char = {
    "firstname": "Demba",
	"lastname": "Bas*7#@",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Markize106"
}

bad_email = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembabagmail.com",
	"phone" : "254712340908",
	"password" : "Markize106"
}

short_email = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "d@g.com",
	"phone" : "254712340908",
	"password" : "Markize106"
}

bad_phone = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "25471234090i",
	"password" : "Markize106"
}

phone_short = {
    "firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "25471234",
	"password" : "Markize106"
}

firstname_not_string = {
	"firstname": 106,
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Macabee106"
}

lastname_not_string = {
	"firstname": "Demba",
	"lastname": 106,
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Macabee106"
}

username_not_string = {
	"firstname": "Demba",
	"lastname": "Basela",
    "username": 106,
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : "Macabee106"
}

email_not_string = {
	"firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": 106,
	"phone" : "254712340908",
	"password" : "Macabee106"
}

phone_not_string = {
	"firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : 254712340908,
	"password" : "Macabee106"
}

password_not_string = {
	"firstname": "Demba",
	"lastname": "Basela",
    "username": "Debasey",
	"email": "dembaba@gmail.com",
	"phone" : "254712340908",
	"password" : 106
}

admin_sign_in = {
    "username": "admin",
	"password" : "Marksman001"
}

user_sign_in = {
    "username": "Debasey",
	"password" : "Macabee106"
}

wrong_password = {
    "username": "Debasey",
	"password" : "Macabee101"

}

user_not_exist = {
    "username": "Lizzzzzzy",
	"password" : "Macabee106"

}

dummy_data = {
    'party': party,
    'office' : office,
    'register': register,
    'vote': vote,
    'same_party': same_party,
    'user_sign_up': user_sign_up,
    'party_less_keys' : party_less_keys,
    'office_less_keys': office_less_keys,
    'hq_add_not_spaces_int_str' : hq_add_not_spaces_int_str,
    'hq_add_no_str' : hq_add_no_str,
    'party_name_blank' : party_name_blank,
    'hqAddress_blank' : hqAddress_blank,
    'logoUrl_blank' : logoUrl_blank,
    'party_name_space' : party_name_space,
    'hqAddress_space' : hqAddress_space,
    'logoUrl_space' : logoUrl_space,
    'office_name_blank': office_name_blank,
    'office_type_blank': office_type_blank,
    'location_blank': location_blank,
    'office_name_space': office_name_space,
    'office_type_space': office_type_space,
    'location_space': location_space,
    'president_location_not_kenya': president_location_not_kenya,
    'prime_min_location_not_kenya': prime_min_location_not_kenya,
    'office_type_not_string': office_type_not_string,
    'office_name_not_string': office_name_not_string,
    'location_not_string': location_not_string,
    'logoUrl_no_scheme': logoUrl_no_scheme,
    'logoUrl_no_netloc': logoUrl_no_netloc,
    'logoUrl_no_path': logoUrl_no_path,
    'edit_party_no_name_key': edit_party_no_name_key,
    'invalid_office_type' : invalid_office_type,
    'office_type_not_letters': office_type_not_letters,
    'office_name_not_letters': office_name_not_letters,
    'location_not_letters': location_not_letters,
    'legislative_mismatch_president' : legislative_mismatch_president,
    'legislative_mismatch_prime_minister' : legislative_mismatch_prime_minister,
    'legislative_mismatch_governor' : legislative_mismatch_governor,
    'legislative_mismatch_mca' : legislative_mismatch_mca,
    'executive_mismatch_governor' : executive_mismatch_governor,
    'executive_mismatch_senator' : executive_mismatch_senator,
    'executive_mismatch_mp' : executive_mismatch_mp,
    'executive_mismatch_women_rep' : executive_mismatch_women_rep,
    'executive_mismatch_mca' : executive_mismatch_mca,
    'county_mismatch_president' : county_mismatch_president,
    'county_mismatch_prime_minister' : county_mismatch_prime_minister,
    'county_mismatch_senator' : county_mismatch_senator,
    'county_mismatch_mp' : county_mismatch_mp,
    'county_mismatch_women_rep' : county_mismatch_women_rep,
    'party_name_not_purely_alpha_and_space' : party_name_not_purely_alpha_and_space,
    'user_sign_up' : user_sign_up,
    'user_less_keys' : user_less_keys,
    'pwd_less_char' : pwd_less_char,
    'pwd_no_caps': pwd_no_caps,
    'pwd_all_caps': pwd_all_caps,
    'pwd_no_digit': pwd_no_digit,
    'firstname_all_char': firstname_all_char,
    'lastname_all_char': lastname_all_char,
    'bad_email': bad_email,
    'short_email': short_email,
    'bad_phone': bad_phone,
    'phone_short': phone_short,
    'admin_sign_in': admin_sign_in,
    'firstname_not_string': firstname_not_string,
    'username_not_string': username_not_string,
    'lastname_not_string': lastname_not_string,
    'email_not_string': email_not_string,
    'phone_not_string': phone_not_string,
    'password_not_string': password_not_string,
    'user_sign_in': user_sign_in,
    'wrong_password': wrong_password,
    'user_not_exist': user_not_exist
}