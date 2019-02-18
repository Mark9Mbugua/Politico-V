party = {
        "party_name": "Jubilee",
        "hqAddress": "Muthaiga",
        "logoUrl": 'https://www.jubilee.com/jubilee/img.jpg'
}

office = {
    'office_type' : "Legislative",
    'office_name': "Member of Parliament"
}

vote = {
    "office_name": "Governor",
    "candidate_id": 1,
    "cd_firstname": "Markize",
    "cd_lastname": "Welar",
    "voter_id": 1
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
    "logoUrl" : "nasa.co.ke" 
}

hqAddress_blank = {
    "party_name": "Jubilee",
    "hqAddress" : "",
    "logoUrl" : "nasa.co.ke" 
}

logoUrl_blank = {
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
    "hqAddress" : "............",
    "logoUrl" : "nasa.co.ke" 
}

hq_add_no_str = {
    "party_name": "Jubilee",
    "hqAddress" : "106106",
    "logoUrl" : "nasa.co.ke" 
}

invalid_office_type = {
    "office_type" : "Cabinet",
    "office_name" : "President"
}

legislative_mismatch_president = {
    "office_type" : "Legislative",
    "office_name" : "President"
}

legislative_mismatch_prime_minister = {
    "office_type" : "Legislative",
    "office_name" : "Prime Minister"
}

legislative_mismatch_governor = {
    "office_type" : "Legislative",
    "office_name" : "Governor"
}

legislative_mismatch_mca = {
    "office_type" : "Legislative",
    "office_name" : "MCA"
}

executive_mismatch_governor = {
    "office_type" : "Executive",
    "office_name" : "Governor"
}

executive_mismatch_senator = {
    "office_type" : "Executive",
    "office_name" : "Senator"
}

executive_mismatch_mp = {
    "office_type" : "Executive",
    "office_name" : "Member of Parliament"
}

executive_mismatch_women_rep = {
    "office_type" : "Executive",
    "office_name" : "Women Rep"
}

executive_mismatch_mca = {
    "office_type" : "Executive",
    "office_name" : "MCA"
}

county_mismatch_president = {
    "office_type" : "County",
    "office_name" : "President"
}

county_mismatch_prime_minister = {
    "office_type" : "County",
    "office_name" : "Prime Minister"
}

county_mismatch_senator = {
    "office_type" : "County",
    "office_name" : "Senator"
}

county_mismatch_mp = {
    "office_type" : "County",
    "office_name" : "Member of Parliament"
}

county_mismatch_women_rep = {
    "office_type" : "County",
    "office_name" : "Women Rep"
}

user_sign_up = {
	"firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "Macabee106"
}

user_less_keys = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
}

pwd_less_char = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "Mac1"
}

pwd_no_caps = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "markize106"
}

pwd_all_caps = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "MARKIZE106"
}

pwd_no_digit = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "Markizeman"
}

firstname_all_char = {
    "firstname": "De*7#@",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "Markize106"
}

lastname_all_char = {
    "firstname": "Demba",
	"lastname": "Bas*7#@",
	"email": "dembaba@gmail.com",
	"phone" : "0712340902",
	"password" : "Markize106"
}

bad_email = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembabagmail.com",
	"phone" : "0712340902",
	"password" : "Markize106"
}

short_email = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "d@g.com",
	"phone" : "0712340902",
	"password" : "Markize106"
}

bad_phone = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "071234090i",
	"password" : "Markize106"
}

phone_not_ten_dig = {
    "firstname": "Demba",
	"lastname": "Basela",
	"email": "dembaba@gmail.com",
	"phone" : "07123409080908",
	"password" : "Markize106"
}

dummy_data = {
    'party': party,
    'office' : office,
    'vote': vote,
    'user_sign_up': user_sign_up,
    'party_less_keys' : party_less_keys,
    'office_less_keys': office_less_keys,
    'hq_add_not_spaces_int_str' : hq_add_not_spaces_int_str,
    'hq_add_no_str' : hq_add_no_str,
    'party_name_blank' : party_name_blank,
    'hqAddress_blank' : hqAddress_blank,
    'logoUrl_blank' : logoUrl_blank,
    'logoUrl_no_scheme': logoUrl_no_scheme,
    'logoUrl_no_netloc': logoUrl_no_netloc,
    'logoUrl_no_path': logoUrl_no_path,
    'edit_party_no_name_key': edit_party_no_name_key,
    'invalid_office_type' : invalid_office_type,
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
    'phone_not_ten_dig': phone_not_ten_dig,
}