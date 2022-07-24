from flask_app import app
from flask import render_template
import urllib.request, urllib.parse, xmltodict, pprint


@app.route('/')
def index():
    print("***********WHOOOOOOOOOO**************")
    return render_template("index.html")

@app.route('/list_of_committees')
def list_of_committees():

    url = "https://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetActiveCommittees"
    response = urllib.request.urlopen(url)
    data = response.read()

    # covert response from xml to a dictionary
    committees = xmltodict.parse(data)
    
    # select relevant node
    # TO DO create Committee Model
    committees = committees['ArrayOfCommittee']['Committee']

    # pretty prints dictionary
    pp = pprint.PrettyPrinter(depth=4)
    print(pp.pprint(committees))
    
    return render_template('list_of_committees.html', committees = committees)

@app.route('/get_committee_members/<agency>/<committee_name>')
def get_committee_members(agency, committee_name):

    # url encode arg strings
    encoded_agency =  urllib.parse.quote(agency)
    encoded_committee_name = urllib.parse.quote(committee_name)
    # build url with encoded strings
    url = "https://wslwebservices.leg.wa.gov/CommitteeService.asmx/GetActiveCommitteeMembers?agency={agency}&committeeName={committee_name}".format(agency=encoded_agency, committee_name=encoded_committee_name)

    response = urllib.request.urlopen(url)
    data = response.read()

    # convert response from xml to a dictionary
    members = xmltodict.parse(data)
    # select relevant node
    members = members['ArrayOfMember']['Member']
    # pretty prints dictionary
    pp = pprint.PrettyPrinter(depth=4)
    print(pp.pprint(members))

    return render_template('committee_members.html', committee_name=committee_name, members=members)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    print(e)
    return "404 not found, bitches", 404