#!/usr/bin/python3.5
# coding:UTF8

#-------------------------  Import package -----------------------------
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import sys
import re
import argparse


def find_broken_links(url, depth) :
    """
    Function that Bbowses all the links contained in a web page and displays the
    broken links.

    :params : args , depth : str
    :return : None
    """

    if depth == 0: # if no depth return none
        pass

    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    links = soup.findAll('a') # list with all html link
    for link in links :
        link_href = link.get('href') # get the reference
        if link_href.startswith('http') or link_href.startswith('https') : # verification if there is protocol
            link_is_broken(link_href)
            find_broken_links(link_href, depth - 1)
        else :
            #new_http_link = urljoin(url + "/",link_href) # create url with protocol
            link_is_broken(urljoin(url + "/",link_href))
            find_broken_links(urljoin(url + "/",link_href), depth - 1) # recursive call


def link_is_broken(link) :
    """
    Functions that allow to know if links are broken

    :param : link : str
    :returns : None
    """
    response = requests.get(link) # request data from the server
    if response.status_code >= 400 : # Asking ressources don't exist
        print("Lien cassé : ", link)
    else :
        pass

def main() :
    """
    The argparse module allows command line interface writing. The program defines
    which arguments are needed, and Argparse will understand how to parse those
    out of sys.argv.Argparse module will automatically pass help and usage messages

    :param file stdin : None
    :returns : None
    """
    parser = argparse.ArgumentParser(description="browses all the links contained in a web page and displays the broken links")
    #=====================>     Link arguments      <============================
    parser.add_argument("url")
    #==================>    optional argument : n(1 by default)     <=============
    parser.add_argument("-d", "--depth", type=int, help="displays the broken list depending the depth")
    arguments = parser.parse_args()
    find_broken_links(arguments.url, arguments.depth)



#-----------------------Main Principal -------------------------------------

if __name__ == '__main__' :

    main()
