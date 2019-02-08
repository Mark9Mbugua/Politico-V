# parties dummy data
party = {
        "party_name": "Jubilee",
        "hqAddress": "Muthaiga",
        "logoUrl": "jubilee.co.ke"
}

# offices dummy data
office = {
    'office_type' : "Legislative",
    'name': "Member of Parliament"
}

party_name_not_str = {
    "party_name": 12345,
    "hqAddress" : "Kinangop",
    "logoUrl" : "nasa.co.ke" 
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

hq_add_not_str = {
    "party_name": "Jubilee",
    "hqAddress" : 123456,
    "logoUrl" : "nasa.co.ke" 
}

logoUrl_not_str = {
    "party_name": "Jubilee",
    "hqAddress" : "Muthaiga",
    "logoUrl" : 323434 
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
    'party_name_not_str' : party_name_not_str,
    'hq_add_not_str' : hq_add_not_str,
    'logoUrl_not_str' : logoUrl_not_str,
    'party_name_blank' : party_name_blank,
    'hqAddress_blank' : hqAddress_blank,
    'logoUrl_blank' : logoUrl_blank,
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