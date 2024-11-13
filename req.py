from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/xinu-main", response_class=PlainTextResponse)
def get_xinu_main():
    code = '''#include <xinu.h>

process main(void)
{
    pid32   shpid;      /* Shell process ID */

    printf("\\n\\n");

    /* Create a local file system on the RAM disk */
    lfscreate(RAM0, 40, 20480);

    /* Run the Xinu shell */
    recvclr();
    resume(shpid = create(shell, 8192, 50, "shell", 1, CONSOLE));

    /* Wait for shell to exit and recreate it */
    while (TRUE) {
        if (receive() == shpid) {
            sleepms(200);
            kprintf("\\n\\nMain process recreating shell\\n\\n");
            resume(shpid = create(shell, 4096, 20, "shell", 1, CONSOLE));
        }
    }
    return OK;
}'''
    return code
