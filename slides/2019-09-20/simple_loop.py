from mpi4py import MPI

comm  = MPI.COMM_WORLD
rank  = comm.Get_rank()
nproc = comm.Get_size()

arr = [1,2,3,4,5,6,7,8]

for i in range(rank, len(arr), nproc):
    print('proc', rank, 'does number', i)
