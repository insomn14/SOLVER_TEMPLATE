; nasm -f elf64 clone2.asm -o clone2.o
; ld -m elf_x86_64 clone2.o -o clone2

global _start
section .data
        msg db "%x", 0xa
        len equ $ - msg

section .text
_start:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16
    mov     dword [rbp-4], 415187
    mov     dword [rbp-8], 0
    jmp     L2
L3:
    mov     eax, dword [rbp-8]
    mov     eax, edx
    sal     eax, 2
    add     eax, edx
    add     eax, eax
    mov     edi, eax
    mov     edx, dword [rbp-4]
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
    lea     eax, dword [rdi+rcx]
    mov     dword [rbp-8], eax
    mov     eax, [rbp-4]
    movsx   rdx, eax
    imul    rdx, rdx, 1717986919
    shr     rdx, 32
    sar     edx, 2
    sar     eax, 31
    mov     ecx, eax
    mov     eax, edx
    sub     eax, ecx
    mov     dword [rbp-4], eax
L2:
    cmp     dword [rbp-4], 0
    jg      L3
    mov     eax, [rbp-8]
    mov     esi, eax
    mov     ebx, eax
    mov     edi, msg
    mov     eax,0
    leave
    ret
