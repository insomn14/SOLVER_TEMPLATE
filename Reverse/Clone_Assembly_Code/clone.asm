global _start
section .data
        msg db "%x", 0xa
        len equ $ - msg

section .text
_start:
    push    ebp
    mov     ebp, esp
    sub     esp, 16
    mov     dword [ebp-4], 415187
    mov     dword [ebp-8], 0
    jmp     L2
L3:
    mov     eax, dword [ebp-8]
    mov     eax, edx
    sal     eax, 2
    add     eax, edx
    add     eax, eax
    mov     edi, eax
    mov     edx, dword [ebp-4]
    mov     edx, edx
    imul    eax, eax, 1717986919
    shr     eax, 32
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
    lea     eax, [edi+ecx]
    mov     [ebp-8], eax
    mov     eax, [ebp-4]
    mov     edx, eax
    imul    edx, edx, 1717986919
    shr     edx, 32
    sar     edx, 2
    sar     eax, 31
    mov     ecx, eax
    mov     eax, edx
    sub     eax, ecx
    mov     [ebp-4], eax
L2:
    cmp     dword [ebp-4], 0
    jg      L3
    mov     eax, [ebp-8]
    mov     ebx, eax
    int     0x80
    mov     eax,0
    leave
    ret
