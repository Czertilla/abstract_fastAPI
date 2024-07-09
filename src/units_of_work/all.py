from repositories.users import UserRepo
from units_of_work._unit_of_work import UnitOfWork

class AllUOW(UnitOfWork):
    async def __aenter__(self):
        rtrn = await super().__aenter__()
        
        self.users = UserRepo(self.session)
        
        return rtrn
