import os
import multiprocessing
import subprocess


def process_products(pid, paths):
    subprocess.run(['run_web_agent_site_env.sh', f"{pid}"], paths)


def main():
    paths = list(range(1, 100))
    total = len(paths)
        
    num_pids = 2
    chunk_size = (int)(total / num_pids)
    chunks = [paths[i:i+chunk_size] for i in range(0, total, chunk_size)]
    processes = []
    for i, chunk in enumerate(chunks):
        process = multiprocessing.Process(target=process_products, args=(i))
        processes.append(process)
        process.start()
    
    for p in processes:
        p.join()


if __name__ == "__main__":
    main()