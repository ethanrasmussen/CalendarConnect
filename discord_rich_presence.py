import schedule
from pypresence import Presence


# set RPC/status
def set_rpc(rpc:Presence, status:str):
    rpc.update(state=status)
    return schedule.CancelJob


# clear RPC/status
def clear_rpc(rpc:Presence):
    rpc.clear()
    return schedule.CancelJob