import argparse

def calculate_beam(length, force, distance):
    """
    Calculates support reactions and max bending moment 
    for a simply supported beam with a single point load.
    """
    # Support reactions
    r_b = (force * distance) / length
    r_a = force - r_b
    
    # Maximum bending moment (under the point of load application)
    max_moment = r_a * distance
    
    print("="*40)
    print("🔥 MechSolve-Core: Calculation Results 🔥")
    print("="*40)
    print(f"Beam length: {length} m")
    print(f"Force: {force} kN applied at {distance} m")
    print("-" * 40)
    print(f"Reaction at Support A (Ra): {r_a:.2f} kN")
    print(f"Reaction at Support B (Rb): {r_b:.2f} kN")
    print(f"Max Bending Moment (M_max): {max_moment:.2f} kN*m")
    print("="*40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fast simply supported beam calculator.')
    parser.add_argument('-l', '--length', type=float, required=True, help='Beam length (m)')
    parser.add_argument('-f', '--force', type=float, required=True, help='Point load force (kN)')
    parser.add_argument('-d', '--distance', type=float, required=True, help='Distance from origin to force (m)')
    
    args = parser.parse_args()
    calculate_beam(args.length, args.force, args.distance)