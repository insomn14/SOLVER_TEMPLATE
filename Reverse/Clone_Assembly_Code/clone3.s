// gcc clone3.s -no-pie -o clone3

.global main
.section .rodata
msg:
    .string "CSCCTF{%X}\n"

.text
main:
    push    %rbp
    mov     %rsp, %rbp
    sub     $16, %rsp
    movl     $415187, -4(%rbp)
    movl     $0, -8(%rbp)
    jmp     L2
L3:
    movl    -8(%rbp), %edx
    mov     %edx, %eax
    sal     $2, %eax
    add     %edx, %eax
    add     %eax, %eax
    mov     %eax, %edi
    mov     -4(%rbp), %edx
    movsx   %edx, %rax
    imul    $1717986919, %rax, %rax
    shr     $32, %rax
    sar     $2, %eax
    mov     %edx, %esi
    sar     $31, %esi
    sub     %esi, %eax
    mov     %eax, %ecx
    mov     %ecx, %eax
    sal     $2, %eax
    add     %ecx, %eax
    add     %eax, %eax
    mov     %edx, %ecx
    sub     %eax, %ecx
    lea     (%rdi,%rcx), %eax
    mov     %eax, -8(%rbp)
    mov     -4(%rbp), %eax
    movsx   %eax, %rdx
    imul    $1717986919,  %rdx
    shr     $32, %rdx
    sar     $2, %edx
    sar     $31, %eax
    mov     %eax, %ecx
    mov     %edx, %eax
    sub     %ecx, %eax
    mov     %eax, -4(%rbp)
L2:
    cmpl    $0, -4(%rbp)
    jg      L3
    mov     -8(%rbp), %eax
    mov     %eax, %esi
    mov     $msg, %edi
    mov     $0, %eax
    call    printf@PLT
    movl    $0, %eax
    leave
    ret
