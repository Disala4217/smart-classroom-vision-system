package com.example.smartclassroomvisionsystem.controllers;
import com.example.smartclassroomvisionsystem.services.LoginService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Map;
@RestController
@RequestMapping("/api")
public class LoginController {
    LoginService loginService=new LoginService();
    @PostMapping("/login")
    public ResponseEntity<Map<String, String>> handleLogin(@RequestBody Map<String, String> data) {
        String ID = data.get("ID");
        String password = data.get("password");
        System.out.println(ID);
        System.out.println(password);
        String name = loginService.LoginUser(ID, password);
        if (name != null) {
            String role=loginService.GetRole(ID);
            String Grade=loginService.GetGrade(ID);
            Map<String, String> response = Map.of("ID", ID, "username", name,"role", role,"Grade",Grade);
            System.out.println(response);
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid credentials"));
        }
    }
}
