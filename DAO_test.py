
from DAO import DAO

id=242

dao=DAO()

print dao.req_zeitreihen([id],DAO.STRESS)
print dao.req_rel_auf([id],DAO.STRESS)
