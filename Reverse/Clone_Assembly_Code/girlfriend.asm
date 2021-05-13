.LC0:
        .string "%x\n"
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], 415187
        mov     DWORD PTR [rbp-8], 0
        jmp     .L2
.L3:
        mov     edx, DWORD PTR [rbp-8]
        mov     eax, edx
        sal     eax, 2
        add     eax, edx
        add     eax, eax
        mov     edi, eax
        mov     edx, DWORD PTR [rbp-4]
        movsx   rax, edx
        imul    rax, rax, 1717986919
        shr     rax, 32
        sar     eax, 2
        mov     esi, edx
        sar     esi, 31
        sub     eax, esi
        mov     ecx, eax
        mov     eax, ecx
        sal     eax, 2
        add     eax, ecx
        add     eax, eax
        mov     ecx, edx
        sub     ecx, eax
        lea     eax, [rdi+rcx]
        mov     DWORD PTR [rbp-8], eax
        mov     eax, DWORD PTR [rbp-4]
        movsx   rdx, eax
        imul    rdx, rdx, 1717986919
        shr     rdx, 32
        sar     edx, 2
        sar     eax, 31
        mov     ecx, eax
        mov     eax, edx
        sub     eax, ecx
        mov     DWORD PTR [rbp-4], eax
.L2:
        cmp     DWORD PTR [rbp-4], 0
        jg      .L3
        mov     eax, DWORD PTR [rbp-8]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, 0
        leave
        ret