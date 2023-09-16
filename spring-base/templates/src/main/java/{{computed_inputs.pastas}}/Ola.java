package br.com.dominio.nomeProjeto;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Ola {
    @GetMapping(path = "/ola")
    public String ola( ) {
        return "Ola";
    }
}
