# parties dummy data
party = {
        "party_name": "Jubilee",
        "hqAddress": "Muthaiga",
        "logoUrl": 'https://www.twitter.com/profile/img.jpg'
}

# offices dummy data
office = {
    'office_type' : "Legislative",
    'name': "Member of Parliament"
}

party_less_keys = {
    "party_name": "Jubilee",
    "hqAddress" : "Kinangop"
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
    "name" : "President"
}

legislative_mismatch_president = {
    "office_type" : "Legislative",
    "name" : "President"
}

legislative_mismatch_prime_minister = {
    "office_type" : "Legislative",
    "name" : "Prime Minister"
}

legislative_mismatch_governor = {
    "office_type" : "Legislative",
    "name" : "Governor"
}

legislative_mismatch_mca = {
    "office_type" : "Legislative",
    "name" : "MCA"
}

executive_mismatch_governor = {
    "office_type" : "Executive",
    "name" : "Governor"
}

executive_mismatch_senator = {
    "office_type" : "Executive",
    "name" : "Senator"
}

executive_mismatch_mp = {
    "office_type" : "Executive",
    "name" : "Member of Parliament"
}

executive_mismatch_women_rep = {
    "office_type" : "Executive",
    "name" : "Women Rep"
}

executive_mismatch_mca = {
    "office_type" : "Executive",
    "name" : "MCA"
}

county_mismatch_president = {
    "office_type" : "County",
    "name" : "President"
}

county_mismatch_prime_minister = {
    "office_type" : "County",
    "name" : "Prime Minister"
}

county_mismatch_senator = {
    "office_type" : "County",
    "name" : "Senator"
}

county_mismatch_mp = {
    "office_type" : "County",
    "name" : "Member of Parliament"
}

county_mismatch_women_rep = {
    "office_type" : "County",
    "name" : "Women Rep"
}

dummy_data = {
    'party': party,
    'office' : office,
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
    
}