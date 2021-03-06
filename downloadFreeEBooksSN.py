# downloadFreeEBooksSN (DOWNLOAD FREE E-BOOKS FROM SPRINGER NATURE) 
# VERSION 1.0 
# COPYRIGHT 2020 PROF MARCELO S ZANETTI
# DISTRIBUTED UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE GPL V3 

# MODULES
from lxml import html 
import sys
import os
import re
import wget
import shutil

# VARIABLES
BOOKS     = []
BASEURL   = "https://link.springer.com"
DB        = ['http://link.springer.com/openurl?genre=book&isbn=978-0-306-48048-5',
'http://link.springer.com/openurl?genre=book&isbn=978-0-306-48247-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-21736-9',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-22592-0',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-21777-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-28117-9',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-24158-6',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-32353-4',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-36218-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-36274-8',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-36601-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-37575-5',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-40065-5',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-45524-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-46271-4',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-46312-4',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-49312-1',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-68566-3',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-72071-5',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-72579-6',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-74365-3',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-75959-3',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-76501-3',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-77650-7',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-78341-3',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-79054-1',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-84858-7',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-87573-6',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-88698-5',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-88963-4',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-93837-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4020-5719-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4020-6099-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4020-6808-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-35963-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-44874-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-03762-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-56194-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-0400-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-27877-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-44794-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-9479-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-18842-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-48936-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-21239-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-7091-0715-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-6488-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-01851-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-3058-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-26551-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-46321-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-13072-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-4556-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4615-1077-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-02099-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-37434-0',
'http://link.springer.com/openurl?genre=book&isbn=978-981-10-2045-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-57040-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-23042-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-53883-9',
'http://link.springer.com/openurl?genre=book&isbn=978-90-481-2516-6',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4899-7454-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-53785-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-51118-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-57589-6',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-1120-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-23026-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-44738-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-05699-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-47831-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-31791-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-54083-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4612-1844-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-84800-070-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-19864-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-61088-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-46162-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-33916-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-32862-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-30250-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-1194-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4613-0139-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-54064-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7116-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-43341-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-0641-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-5653-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-12682-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-7307-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-53045-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-33143-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-31089-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-12742-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-52250-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-5134-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-28887-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-9504-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-45171-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-8349-6331-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-84882-935-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-07806-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-14142-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-37314-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-20951-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-50091-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-77974-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-19596-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-53022-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-4474-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-54413-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-37902-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-46394-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-6374-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4612-4374-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-59731-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-22309-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-30319-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-2212-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-49887-3',
'http://link.springer.com/openurl?genre=book&isbn=978-94-007-5757-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-14941-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2122-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-58307-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6271-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-21936-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-09351-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-21990-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-9170-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-55309-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-5201-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2614-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-20451-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4612-4360-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-09171-6',
'http://link.springer.com/openurl?genre=book&isbn=978-94-007-1171-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-23012-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-4809-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-0925-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-658-07884-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-27265-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-57883-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-31650-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-01195-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-54349-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-43715-5',
'http://link.springer.com/openurl?genre=book&isbn=978-981-4560-67-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-23428-1',
'http://link.springer.com/openurl?genre=book&isbn=978-94-007-1211-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-27104-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-55444-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-63913-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-44561-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-34132-8',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-3954-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-29854-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-55615-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-46407-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-9982-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-53919-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-24551-5',
'http://link.springer.com/openurl?genre=book&isbn=978-981-10-1802-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-6419-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-6572-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-84800-322-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6940-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4612-0979-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-11080-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-30304-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-29716-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-04101-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-24346-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4613-0041-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2712-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-76504-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7630-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-33405-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-31036-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-1151-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-40975-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-3618-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-10091-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-3523-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-62872-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-56475-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-5538-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-00401-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-03623-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-19464-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-20556-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6227-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-54398-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-15018-5',
'http://link.springer.com/openurl?genre=book&isbn=978-94-017-8771-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2113-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-22951-5',
'http://link.springer.com/openurl?genre=book&isbn=978-4-431-54526-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-6646-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-65867-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7138-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-00894-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-44048-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-12493-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-9236-8',
'http://link.springer.com/openurl?genre=book&isbn=978-981-287-212-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-28980-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-29791-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-84628-642-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-20059-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-51412-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-20600-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-19425-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-54817-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-44127-6',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6786-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-24331-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-50651-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-54486-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-3987-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-93804-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-8933-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-50319-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-39439-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-57750-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-05290-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-01769-3',
'http://link.springer.com/openurl?genre=book&isbn=978-94-007-6863-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-0867-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-84628-168-6',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4419-7288-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-69934-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-49810-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-14240-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-21173-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-658-10183-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-45776-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-1911-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-15195-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7807-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4757-0576-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-29659-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6486-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-6642-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4899-7550-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-32899-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-24280-4',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-3143-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-19587-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2623-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-540-27752-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-50017-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7946-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-61185-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-46950-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-18539-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-16874-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-25970-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6849-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-34195-8',
'http://link.springer.com/openurl?genre=book&isbn=978-94-017-7242-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-15666-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-23880-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-49875-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-18398-5',
'http://link.springer.com/openurl?genre=book&isbn=978-94-007-6113-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2766-1',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-2197-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-14777-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-9138-5',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4612-1272-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-5361-0',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-5601-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4471-6684-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-9126-2',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4757-2519-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-55606-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-57252-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-25675-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-8687-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-642-20144-8',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4614-4262-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-44899-2',
'http://link.springer.com/openurl?genre=book&isbn=978-0-387-71481-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-14454-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-48848-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-49849-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-58715-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-64786-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-65451-5',
'http://link.springer.com/openurl?genre=book&isbn=978-981-10-5218-7',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-6676-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-61158-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-66631-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-70920-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-70790-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-63133-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-49279-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-64410-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-66772-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-68588-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-68598-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72547-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-58487-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-67395-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-65439-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-73004-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-66219-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-75771-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-73123-0',
'http://link.springer.com/openurl?genre=book&isbn=978-94-024-1144-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-56272-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-56509-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-68834-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-73132-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-65094-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72682-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-59978-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-65682-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-77649-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-76442-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-78729-9',
'http://link.springer.com/openurl?genre=book&isbn=978-1-349-95348-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-68301-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-78361-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-77809-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-55381-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-77425-1',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-0399-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-91041-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-74965-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-57265-8',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-1090-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-78181-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-89491-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-91722-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72911-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-91575-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-92207-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-95381-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-63588-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-91890-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-89292-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72314-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-75502-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-75708-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-92804-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-94463-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72347-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-92429-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-95762-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-92333-8',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-2475-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-56707-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-94313-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-98833-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-97298-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-02405-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-77434-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-91155-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-96622-9',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-96713-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-00581-8',
'http://link.springer.com/openurl?genre=book&isbn=978-981-10-8297-9',
'http://link.springer.com/openurl?genre=book&isbn=978-981-10-8321-1',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-0785-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-75804-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-99516-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-99118-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-02604-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-03255-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-94743-3',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-2023-1',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-00464-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-77315-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-00467-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-01279-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-04516-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-99420-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-71288-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-72000-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-05609-4',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-74373-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-96337-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-05900-2',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-6643-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-10552-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-98875-7',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-12489-2',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-3621-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-74746-0',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-13005-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-13605-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-00710-2',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-12727-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-13020-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-15671-8',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-11117-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-15224-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-18435-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-13788-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-319-68837-4',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-7496-8',
'http://link.springer.com/openurl?genre=book&isbn=978-981-13-8759-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-19182-5',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-20290-3',
'http://link.springer.com/openurl?genre=book&isbn=978-3-030-25943-3',
'http://link.springer.com/openurl?genre=book&isbn=978-1-4939-9621-6',
'http://link.springer.com/openurl?genre=book&isbn=978-3-662-56233-8']

# FUNCTIONS
def download_book(url):
	try:	
		n_tries = 0
		while True:	
			try:
				page = html.open_http_urllib('GET',url,'')
				break
			except Exception as e:	
				n_tries += 1
				if n_tries==10:
					return "ERROR: "+str(e)+"|0"	
	
		doc = html.fromstring( page.read() )
	
		rexpt = re.compile("[ \\\\/\-]")		
		
		title = doc.xpath("//div[@data-test='book-title']//text()")
		for i in range(0,len(title)):
			title[i] = title[i].strip().replace(",","")
		title   = rexpt.sub("_", "_".join(title).strip(" _"))
		s_title = title[:60]	
		
		rexpa = re.compile("[\\\\/]")		
		
		autor   = doc.xpath("//ul/li/span[@itemprop='name']")     
		autor   = rexpa.sub("_",autor[0].text)		
		autor   = autor.split()
		nautor  = len(autor)
		autor   = autor[nautor-1].strip(" _-")	
		s_autor = "_"+autor[:20]
	
		rexpf = re.compile("[\(\),®:.—'\"?*<>|!;]")
		
		filename = s_title+s_autor
		filename = rexpf.sub("",filename).replace("&","and").replace("@","at")
		
		link = doc.xpath("//div/a[@title='Download this book in PDF format']")
		if link==None or len(link)==0:
			raise Exception("Not downloadable : check springer site at %s"%url)
		link = link[0].get('href')  
		if link.find("pdf")<0:
			raise Exception("Not a pdf file : check springer site at %s"%url)
		if link.find("http")<0:		
			link = BASEURL+link
		
		if not os.path.exists("books"):
			os.mkdir("books")
		
		ind = ""	
		px  = ""	
		while os.path.exists("books/%s%s%s.pdf"%(filename,px,ind)):		
			if ind=="":	
				ind  = 1
				px   = "_"
			else:
				ind += 1
		
		n_tries = 0		
		while True:	
			try:
				wget.download(link,"books/%s%s%s.pdf"%(filename,px,ind),bar=None)
				break
			except Exception as e:	
				n_tries += 1
				if n_tries==10:
					return "ERROR: "+str(e)+"|0"

		return "DONE: "+title+" "+autor+"|1"

	except Exception as e:
		return "ERROR: "+str(e)+" "+title+" "+autor+"|0"

if __name__=="__main__":
#===============================================================================
	if len(sys.argv)==2: 
		try:
			BOOKS.extend(open(sys.argv[1]).readlines()) 
		except:
			print("ERROR: %s NOT FOUND...WILL NOT PROCEED"%sys.argv[1])
			exit()
	else:	
		BOOKS.extend(DB)
		sp_available = shutil.disk_usage(os.getcwd())[2]
		if sp_available < 8787838196:
			print("ERROR: THIS DOWNLOAD REQUIRES AT LEAST 8.2GB OF FREE SPACE...WILL NOT PROCEED")
			exit()
			
	print("RUNNING...", end = '', flush=True)	
	opdf        = open("log.txt","w",1)
	N           = len(BOOKS)
	downloaded  = 0	
	for book in range(0,N):
		r,s = download_book(BOOKS[book].strip()).split("|")
		downloaded += int(s)
		opdf.write("%3d of %d %s\n"%(book+1,N,r))
		print("\rRUNNING...%5.1f%% COMPLETE - %d of %d BOOKS DOWNLOADED"%(100*(book+1)/N,downloaded,N), end = '')
	
	opdf.close()	

	print("\nDOWNLOAD CONCLUDED! SEE log.txt FOR INFO")
