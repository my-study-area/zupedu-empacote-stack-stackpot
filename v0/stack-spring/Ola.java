package br.com.dominio.nomeProjeto;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Ola {
    private UsuarioRepository respository;

    public Ola(UsuarioRepository respository) {
        this.respository = respository;
    }

    @GetMapping(path = "/ola")
    public String ola( ) {
        respository.save(new Usuario("fulano"));
        return "Ola";
    }
}
